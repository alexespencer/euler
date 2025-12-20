# Read in the pyramid
pyramid = []
with open("data/p67.txt", "r") as f:
    for line in f:
        pyramid.append(list(map(int, line.split())))

# From the bottom up "eat" each layer and a number becomes max(itself + left, itself + right)
# Do this until we 1 layer left
# To make this easier, reverse the pyramid layers
pyramid.reverse()

previous_layer = None
for layer in pyramid:
    if previous_layer is None:
        previous_layer = layer
        continue

    for i in range(len(layer)):
        left = previous_layer[i]
        right = previous_layer[i + 1]
        layer[i] = max(layer[i] + left, layer[i] + right)

    previous_layer = layer

print(previous_layer[0])
