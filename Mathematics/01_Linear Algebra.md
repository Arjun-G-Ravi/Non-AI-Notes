# Linear Algerba
Linear algebra is our 'good old algebra' that focuses on the study of vector spaces and linear mappings between those spaces. Algebraic representation of linear algebra problems will be linear equations. Geometrically, there will be no curves. 

## Vector Spaces
A vector space is a set of vectors that satisfies certain algebraic properties. These properties include closure under vector addition and scalar multiplication, associativity, commutativity, and the existence of additive and multiplicative identities.

# 1. Linear System of Equations

## Solution
Value of variable that satisfies multiple linear eqn is called the solution of the system of eqns. Geometrically, this solution will be on the intersection of the geometrical eqns(which can be lines, planes or hyperplanes).

## Matrix
A matrix is a two-dimensional array of numbers, symbols, or expressions, arranged in rows and columns. Matrix is vastly exploited by linear algebra to represent 
 - Systems of linear equations
 - Linear transformations
 - Eigenvalues and Eigenvectors, etc

## Representation in Matrix form
Matrix can be used to reperesent a system of liner equations as:
![Local Image](images/image1.png)
In the image, the vectors are represented as rows in the matrix. You can also use columns as vectors - it is only a matter of convinience.

Now, a system of linear eqns can be represented by using matrix using **A@X = B**, where @ refers to matmul.
Here, the equation can have:
 - No soln: B is not in the *span* of A.
 - One soln: The vectors are independent
 - Inf soln: Some of the vectors are dependent 


This representation can be changed to augmented matrix, and then represented in row echlon form. While doing all this, we can do three operations which will not change the solution set
 - Multiply a row with a scalar
 - Add/sub a row with the multiple of another row
 - Interchange rows

**Rank**: Number of non-zero rows in echlon form.

if rank(A) == rank(augmented matrix) after converting both to row echlon form, then the system of linear eqns represented by the matrix is independent.

## Row echlon form
Row echlon form of a matrix is a minimised version of the matrix that retains the same solutions as the base matrix (base set of vectors). Converting to this form can be helpful when doing matmul manully. There can be multiple row echlon form of a single matrix.
![Local Image](images/image2.png)

In row echlon form, the vectors are **generally** represented as rows in the coefficient matrix. Row operations are applied to the rows of the matrix to achieve the desired form, and the columns remain unchanged during this process.

# 3. Vectors
A vector is a mathematical object used to represent quantities that have both magnitude and direction. 
There are (at least) three different ways to think about vectors: a vector as an array of numbers (a computer science view), a vector as an arrow with a direction and magnitude (a physics view), and a vector as an object that obeys addition and scaling (a mathematical view).

## Representation of vectors
 - In linear algebra, column vector form is often used when defining vectors, especially when working with matrix-vector multiplication because it aligns well with the matrix structure.
 - In physics, it's common to use row vector form for quantities like position vectors, which makes it easier to perform dot products with other vectors.
 - In computer programming, the choice may depend on the programming language and libraries being used.
 - **Generally, vectors can be represented as row or column depending on the context and ease of notation.** 

## Properties of vectors
 - Scalar multiplication (stretching)
 - Vector Addition

## Span
A linear combination of vectors is a mathematical operation that involves multiplying each vector by a scalar (a real number) and then adding the results together.
The **span** of a set of vectors refers to the set of all possible vectors that can be obtained by the linear combination of the given vectors.
The **Basis vectors** of a vector space refers to a set of linearly independent vectors that span the entire vector space.