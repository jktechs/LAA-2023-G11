import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
])

# Perform Singular Value Decomposition
U, S, Vt = np.linalg.svd(A)

# Extract the first two columns of U and Vt
U1_2 = U[:, :2]
V1_2 = Vt[:2, :]

# Ensure all elements in U1_2 and V1_2 are non-negative
U1_2 = np.abs(U1_2)
V1_2 = np.abs(V1_2)

# Projection of terms onto U1_2
terms_projection = np.dot(U1_2.T, np.eye(A.shape[0]))

# Projection of documents onto V1_2
documents_projection = np.dot(V1_2, np.eye(A.shape[1]))

# Normalize the projections to have norms <= 1
terms_projection /= np.linalg.norm(terms_projection, axis=0)
documents_projection /= np.linalg.norm(documents_projection, axis=0)

# Now, terms_projection and documents_projection contain the desired projections
# terms_projection[:, j] represents the projection of the j-th term onto U1_2
# documents_projection[:, j] represents the projection of the j-th document onto V1_2


# Normalize the projections to have norms <= 1
terms_projection /= np.linalg.norm(terms_projection, axis=0)
documents_projection /= np.linalg.norm(documents_projection, axis=0)

# Now, terms_projection and documents_projection contain the desired projections
# terms_projection[:, j] represents the projection of the j-th term onto U1_2
# documents_projection[:, j] represents the projection of the j-th document onto V1_2

# Plot terms_projection
plt.figure(figsize=(8, 6))
plt.scatter(terms_projection[0, :], terms_projection[1, :], marker='o')

# Add labels for each customer
for i, customer in enumerate(['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5', 'Customer 6', 'Customer 7', 'Customer 8', 'Customer 9', 'Customer 10']):
    plt.text(terms_projection[0, i], terms_projection[1, i], customer, fontsize=8)

# Set plot limits
plt.xlim([0, 1])
plt.ylim([-1, 1])

# Set axis labels and title
plt.xlabel('U1_2 Dimension 1')
plt.ylabel('U1_2 Dimension 2')
plt.title('Projection of Customers onto U1_2')

# Display the plot
plt.show()

# Plot documents_projection
plt.figure(figsize=(8, 6))
plt.scatter(documents_projection[0, :], documents_projection[1, :], marker='o')

# Add labels for each grocery item
for i, grocery_item in enumerate(['Bread', 'Milk', 'Eggs', 'Cheese', 'Yogurt', 'Coffee', 'Cereal', 'Juice', 'Snacks', 'Shampoo']):
    plt.text(documents_projection[0, i], documents_projection[1, i], grocery_item, fontsize=8)

# Set plot limits
plt.xlim([0, 1])
plt.ylim([-1, 1])

# Set axis labels and title
plt.xlabel('V1_2 Dimension 1')
plt.ylabel('V1_2 Dimension 2')
plt.title('Projection of Grocery Items onto V1_2')

# Display the plot
plt.show()
