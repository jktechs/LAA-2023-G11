using LinearAlgebra
using Random

elapsed_time = @elapsed begin
A = rand(10000, 10000)
b = rand(10000)
end

println("elapsed time to create a random n = 1000 matrix and vector: $elapsed_time seconds")

elapsed_time = @elapsed begin
x = A \ b
end

println("elapsed time to solve Ax = b: $elapsed_time seconds")

elapsed_time = @elapsed begin
eig = eigen(A)
end

println("elapsed time to find eigenvalues of A: $elapsed_time seconds")

elapsed_time = @elapsed begin
svd_A = svd(A)
end

println("elapsed time to find singular values of A: $elapsed_time seconds")