import pyaudio
import numpy as np
import time

# 音频参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # 采样率
CHUNK = 2**15  # 增加块大小以提高频率分析的精度

# 初始化PyAudio
p = pyaudio.PyAudio()

# 打开音频流
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

print("正在监听麦克风输入...")

# 在 while 循环前添加变量保存上次输出
last_output = "等待音频输入..."

# 音名映射函数
def frequency_to_note(freq):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    if freq < 20:  # 低于人耳听觉范围
        return "N/A"
    semitones_from_C0 = 12 * np.log2(freq / 16.35)  # 16.35 Hz 是 C0 的频率
    note_index = int(round(semitones_from_C0)) % 12
    octave = int(round(semitones_from_C0) // 12)
    return f"{notes[note_index]}{octave}"

try:
    while True:
        try:
            # 读取音频数据
            data = stream.read(CHUNK, exception_on_overflow=False)
            
            # 将音频数据转换为NumPy数组
            audio_data = np.frombuffer(data, dtype=np.int16)
            
            # 应用汉明窗以减少频谱泄漏
            window = np.hamming(len(audio_data))
            audio_data = audio_data * window
            
            # 计算音频强度（RMS）
            rms = np.sqrt(np.mean(audio_data**2))
            intensity = min(int(rms), 100)
            
            # 计算频率（使用FFT）
            fft_data = np.fft.rfft(audio_data)
            fft_freq = np.fft.rfftfreq(len(audio_data), 1.0/RATE)
            fft_abs = np.abs(fft_data)
            
            # 限制频率范围在20 Hz到20 kHz之间
            valid_mask = (fft_freq >= 20) & (fft_freq <= 20000)
            valid_fft = fft_abs[valid_mask]
            valid_freqs = fft_freq[valid_mask]
            
            if len(valid_fft) > 0:
                # 找出前7个最强的频率分量
                top_indices = np.argsort(valid_fft)[-7:][::-1]
                top_freqs = [int(valid_freqs[i]) for i in top_indices]
                top_intensities = [int(valid_fft[i] / np.max(valid_fft) * 100) for i in top_indices]
                
                # 使用简单的噪声门限
                if intensity > 60:
                    # 清除之前的输出并显示新数据
                    print('\033[H\033[J', end='')  # 清屏
                    output_lines = [
                        f"频率 {i+1}: {freq:5d} Hz ({frequency_to_note(freq)}) | 相对强度: {strength:3d}%" 
                        for i, (freq, strength) in enumerate(zip(top_freqs, top_intensities))
                    ]
                    last_output = '\n'.join(output_lines)  # 保存当前输出
                    print(last_output)
                else:
                    # 显示上次的输出结果
                    print('\033[H\033[J', end='')  # 清屏
                    print(f"环境过于安静...\n上次检测结果:\n{last_output}")
            else:
                print('\033[H\033[J', end='')  # 清屏
                print(f"未检测到有效频率范围内的声音\n上次检测结果:\n{last_output}")
            
            time.sleep(0.01)  # 稍微增加延迟以减少闪烁
            
        except IOError as e:
            print(f"音频输入错误: {e}", end='\r')
            continue
        except Exception as e:
            print(f"处理错误: {e}", end='\r')
            continue

except KeyboardInterrupt:
    print("\n停止监听...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("程序已结束")