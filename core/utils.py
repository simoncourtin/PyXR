def encodeToSRGB(v):
	if (v <= 0.0031308):
		return (v * 12.92) * 255.0
	else:
		return (1.055*(v**(1.0/2.4))-0.055) * 255.0

def encodeRelativeLuminance(r,g, b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def minmax(_min, _max, value):
    return max(min(value, _max), _min)