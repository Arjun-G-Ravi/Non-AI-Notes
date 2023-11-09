# Linear Algerba
Linear algebra is our 'good old algebra' that focuses on the study of vector spaces and linear mappings between those spaces. Algebraic representation of linear algebra problems will be linear equations. Geometrically, there will be no curves. 

# 1. Matrix
A matrix is a two-dimensional array of numbers, symbols, or expressions, arranged in rows and columns. Matrix is vastly exploited by linear algebra to represent 
 - Systems of linear equations
 - Linear transformations
 - Eigenvalues and Eigenvectors, etc

### Inverse of a matrix
For a matrix A, if A@B == I == B@A, then B is the inverse of A.
The matrix whose inverse exists is called Regular/ Non Singular/ Invertible matrix. 

### Transpose
Transpose of a matrix is obtained by interchanging its rows and columns.

# 2. Vectors
A vector is a mathematical object used to represent quantities that have both magnitude and direction. 
There are (at least) three different ways to think about vectors: 
 - a vector as an array of numbers (a computer science view)
 - a vector as an arrow with a direction and magnitude (a physics view)
 - a vector as an object that obeys addition and scaling (a mathematical view).
Polynomials are also (unusual) instances of vectors, as they obey the mathematical view.

### Properties of vectors
 - Scalar multiplication (stretching)
 - Vector Addition

### Representation of vectors
 - In linear algebra, column vector form is often used when defining vectors, especially when working with matrix-vector multiplication because it aligns well with the matrix structure.
 - In physics, it's common to use row vector form for quantities like position vectors, which makes it easier to perform dot products with other vectors.
 - In computer programming, the choice may depend on the programming language and libraries being used.
 - **Generally, vectors can be represented as row or column depending on the context and ease of notation.** 

# 3. Vector Spaces
In mathematics, a vector space is an algebraic structure that consists of a set of vectors, along with two operations: vector addition and scalar multiplication.
It is a set, and every element in it is a vector.
**The concept of a vector space is foundational in linear algebra because it provides the mathematical framework and environment in which linear algebraic operations and transformations take place.**
The **Basis vectors** of a vector space refers to a set of linearly independent vectors that span the entire vector space.

### Span of a vector
The span of a set of vectors refers to the set of all possible vectors that can be obtained by the linear combination of the given vectors.

### Vector Subspace
They are sets contained in the original vector space with the property that when we perform vector space operations on elements within this subspace, we will never leave it.
Thus, vector subspaces are 'closed' under vector addition and scalar multiplication.

### Linear Independence
In linear algebra, a set of vectors is said to be "linearly independent" if none of the vectors in the set can be expressed as a linear combination of the others. 
Geometrically, linearly independent vectors in n-dimensional space do not lie in the same hyperplane. Intuitively, a set of linearly independent vectors consists of vectors that have no redundancy, i.e., if we remove any of those vectors from the set, we will lose something.

### Linear Combination of vectors
A linear combination of vectors is a mathematical operation that involves multiplying each vector by a scalar (a real number) and then adding the results together.

### Generating set
A set of vectors which spans the vector space.

### Basis
A set of linearly independent vectors that spans the vector space. It is the minimal generating set.
Every vector space has a basis. The dimension of a vector space is the length of its basis.
For eg, i,j,k are a basis of the cartesian coordinate system.

### Rank
The number of linearly independent columns of a matrix equals the number of linearly independent rows and is called the rank of A and is denoted by rk(A).
It is the number of non-zero rows in echlon form.

# 4. Linear System of Equations
### Solution to a S.O.L.E
Value of variable that satisfies multiple linear eqn is called the solution of the system of eqns. Geometrically, this solution will be on the intersection of the geometrical eqns(which can be lines, planes or hyperplanes).

### Representation of a S.O.L.E in Matrix form
Matrix can be used to reperesent a system of liner equations as:
![Local Image](images/image1.png)
In the image, the vectors are represented as rows in the matrix. You can also use columns as vectors - it is only a matter of convinience.

Now, a system of linear eqns can be represented by using matrix using **A@X = B**, where @ refers to matmul. This can be solved to obtain the soln of the S.O.L.E.
Here, the equation can have:
 - No soln : B is not in the *span* of A's.
 - One soln: The vectors are independent.
 - Inf soln: Some of the vectors are dependent.

### Row Echlon Form
Row echlon form of a matrix is a minimised version of the matrix that retains the same solutions as the base matrix (base set of vectors). Converting to this form can be helpful when doing matmul manully. There can be multiple row echlon form of a single matrix.
![Local Image](images/image2.png)

The matrix representation of a S.O.L.E can be changed to augmented matrix, and then represented in row echlon form. To do that, we can do three operations which will not change the solution set. They are called elementary transformations:
 - Multiply a row with a scalar
 - Add/sub a row with the multiple of another row
 - Interchange rows

If rank(A) == rank(augmented matrix) after converting both to row echlon form, then the system of linear eqns represented by the matrix is independent.
In row echlon form, the vectors are **generally** represented as rows in the coefficient matrix. Row operations are applied to the rows of the matrix to achieve the desired form, and the columns remain unchanged during this process.