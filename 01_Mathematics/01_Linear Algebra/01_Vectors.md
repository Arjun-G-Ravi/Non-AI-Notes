# Vectors
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

## Important Vectors
- A zero vector is a vector with all elements equal to zero. It has no magnitude, and arbitary direction.
- A unit vector has a magnitude of one and a particular direction.
- A vector is said to be sparse if many of its entries are zero
- Vectors v1 and v2 are mutually orthogonal if they make an angle of 90 between them. Then, ```v1.v2 = 0, for v1 != v2```


## Linear Combination of vectors
A linear combination of vectors is a mathematical operation that involves multiplying each vector by a scalar (a real number) and then adding the results together.

### Linear Independence
In linear algebra, a set of vectors is said to be "linearly independent" if none of the vectors in the set can be expressed as a linear combination of the others. 
Geometrically, linearly independent vectors in n-dimensional space do not lie in the same hyperplane. Intuitively, a set of linearly independent vectors consists of vectors that have no redundancy, i.e., if we remove any of those vectors from the set, we will lose something.
When represented in matrix form, all column vectors are linearly independent if and only if all columns are pivot columns. If there is at least one non-pivot column, the columns (and, therefore, the corresponding vectors) are linearly dependent.

## Inner product
A positive definite, symmetric bilinear mapping Ω : V ×V → R is called an inner product on V. Dot product is a type of inner product.

## Dot product
The dot product, also known as the scalar product, is a binary operation that takes two equal-length sequences of numbers (usually coordinate vectors) and returns a single number.

![Alt text](<Screenshot from 2023-12-25 11-01-29.png>)
![Alt text](<Screenshot from 2023-12-25 11-01-42.png>)

`Graphically, it is the product of the length of one vector with the projection of the other vector on the first vector`. It can be used to evaluate how aligned two vectors are. It is also used to evaluate angle between vectors.


## Norm
The norm of a vector, often denoted by ‖v‖ is a measure of the length or magnitude of the vector. 
Eg: Manhattan Norm (L1 norm), Euclidean Norm (L2 norm), etc.

## Projection
Projection, in mathematics, refers to the process of mapping a vector onto a subspace. The most common type of projection is the orthogonal projection, which involves projecting a vector onto a subspace in a way that the projected vector is orthogonal (perpendicular) to the subspace. 
Orthogonal projections are used in ML to visualise a higher dimensional graph, without the loss of valuable information. PCA works with this.




















## FLOP/s
Vectors are stored as arrays of floating point numbers (or integers, when the entries are all integers). Storing an n-vector requires 8n bytes to store. Sparse vectors are stored in a more efficient way that keeps track of indices and values of the nonzero entries.

When computers carry out addition, subtraction,multiplication, division, or other arithmetic operations on numbers represented in floating point format, the result is rounded to the nearest floating point number.The very small error in the computed result is called (floating point) round-off error.These operations are called floating point operations.

A very rough estimate of the time required to carry out some computation, such as an inner product, can be found by counting the total number of floating point operations, or FLOPs. This is generally useful in evaluating complexity of algorithm and quality of hardware used.







