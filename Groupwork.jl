using LinearAlgebra
G = rand(0:1, 10, 10)
G[diagind(G)] .= 0
G
norms = norm.(eachcol(G), 1)
norms = 1 ./ norms
A = diagm(norms)
Z = G * A

F = (Z * 0.85) + fill(0.15 / size(Z, 1), size(Z))


using Latexify
using Printf

latexify(G)
F_round = round.(F, digits=3)
Z_round = round.(Z, digits=3)
F_parse = [parse(Float64, @sprintf("%.2f", x)) for x in F]
Z_parse = [parse(Float64, @sprintf("%.2f", x)) for x in Z]
latexify(Z_round)

latexify(F_round)
F