import torch 


# Create two sample tensors
tensor_a = torch.tensor([[1, 2], [3, 4]])
tensor_b = torch.tensor([[5, 6], [7, 8]])

# Element-wise addition
addition = tensor_a + tensor_b
print("Addition:\n", addition)

# Element-wise multiplication
multiplication = tensor_a * tensor_b
print("\nElement-wise Multiplication:\n", multiplication)

# Matrix Multiplication (Dot product)
matmul = torch.matmul(tensor_a, tensor_b)
print("\nMatrix Multiplication:\n", matmul)

# Transposing a tensor (swapping rows and columns)
transposed = tensor_a.T
print("\nTransposed Tensor:\n", transposed)