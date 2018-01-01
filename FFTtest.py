# -*- coding:utf-8 –*-
import numpy as np
import matplotlib.pyplot as plt

# single frequency signal
# 采样频率 (sampling_rate) 确定的情况下，取波形中的 fft_size 个数据进行 FFT 变换时，
# 若这 fft_size 个数据包含整数个周期，FFT 所计算的结果是精确的。
# 即当被采样频率 f 满足如下公式时，FFT 的计算结果是精确的。
# f = n * (sample_rate / fft_size)
sampling_rate = 2**13
fft_size = 2**10
t = np.arange(0, 1, 1.0/sampling_rate)
x = np.array(map(lambda x : x*1e3, t))
y = np.sqrt(2)*np.sin(2*np.pi*1000*t)
y = y + 0.005*np.random.normal(0.0,1.0,len(y))
# fft
# np.fft库中提供了一个rfft函数，它方便我们对实数信号进行FFT计算。
# 根据FFT计算公式，为了正确显示波形能量，还需要将rfft函数的结果除以fft_size：
ys = y[:fft_size]
yf = np.fft.rfft(ys)/fft_size
# rfft函数的返回值是N/2+1个复数，分别表示从0(Hz)到sampling_rate/2(Hz)的N/2+1点频率的成分。
# 于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
freq = np.linspace(0,sampling_rate/2, fft_size/2+1)
freqs = np.array(map(lambda x : x/1e3, freq))
# 并通过 20*np.log10() 将其转换为以db单位的值。
# 为了防止0幅值的成分造成log10无法计算，我们调用np.clip对xf的幅值进行上下限处理：
yfp = 20*np.log10(np.clip(np.abs(yf),1e-20,1e100))

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.plot(x[:160], y[:160])
ax1.plot(freq / 1000, yfp)
ax1.set_xlabel('Frequency [KHz]')
plt.show()