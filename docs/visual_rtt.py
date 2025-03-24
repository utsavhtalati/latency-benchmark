import matplotlib.pyplot as plt

# Example data for message sizes and RTTs (replace with actual data)
message_sizes = [64, 128, 512, 1024, 2048, 4096]
rtts = [0.001766, 0.000275, 0.00320, 0.000275, 0.000267, 0.000087]  # Replace with actual RTT values

plt.plot(message_sizes, rtts, marker='o')
plt.title('RTT vs. Message Size')
plt.xlabel('Message Size (bytes)')
plt.ylabel('Round-trip Time (seconds)')
plt.grid(True)
plt.show()
