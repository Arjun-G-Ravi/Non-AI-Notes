# Matrix
A matrix is a two-dimensional array of numbers, symbols, or expressions, arranged in rows and columns. It is generally used to store collection of (related) vectors. Matrix is vastly exploited by linear algebra to represent: 
 - Systems of linear equations
 - Linear transformations
 - Eigenvalues and Eigenvectors, etc

### Inverse of a matrix
For a matrix A, if ```A@B == I == B@A``` then B is the inverse of A.
The matrix whose inverse exists is called Regular/ Non Singular/ Invertible matrix. 

### Transpose
Transpose of a matrix is obtained by interchanging its rows and columns.

## Operations
 - Matrix Addition/ Element-wise addition
 - Scalar Multiplication
 - Matrix multiplication

# Vector Space
In mathematics, a vector space is an algebraic structure that consists of a set of vectors, along with two operations: vector addition and scalar multiplication.
It is a set where every element in it is a vector.
**The concept of a vector space is foundational in linear algebra because it provides the mathematical framework and environment in which linear algebraic operations and transformations take place.**

## Span
The span of a set of vectors refers to the set of all possible vectors that can be obtained by the linear combination of the given vectors.

### Vector Subspace
They are sets contained in the original vector space with the property that when we perform vector space operations on elements within this subspace, we will never leave it.
Thus, vector subspaces are 'closed' under vector addition and scalar multiplication.

### Generating set
A set of vectors which spans the vector space. The minimal generating set is called basis.

### Basis
A set of linearly independent vectors that spans the vector space. Every vector space has a basis. The dimension of a vector space is the length of its basis.
For eg, i,j,k are a basis of the cartesian coordinate system.
The dimension of a vector space is equal to the number of its basis vectors.

# Matrix decomposition
Matrix decomposition, also known as matrix factorization, refers to the process of expressing a matrix as a product of two or more matrices, often with specific properties. These factorized matrices can provide insights into the structure of the original matrix and are useful in various mathematical and computational applications. 

### Trace
The sum of diagonal elements of a matrix.

# Determinant
The determinant is a scalar value that can be calculated from the elements of a square matrix. It has several important applications, particularly in solving systems of linear equations, finding eigenvalues, and understanding linear transformations.
`It is the factor by which a transformation matrix changes the area of shape/volume of parallelogram/parallelopiped, after transformation.`

![Alt text](<Screenshot from 2023-12-17 09-04-00.png>)

### Some properties on determinant
![Alt text](<Screenshot from 2023-12-17 09-06-55.png>)


