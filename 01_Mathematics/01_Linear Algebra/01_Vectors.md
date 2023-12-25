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

## Linear Combination of vectors
A linear combination of vectors is a mathematical operation that involves multiplying each vector by a scalar (a real number) and then adding the results together.

## Dot/Inner product
The dot product, also known as the scalar product or inner product, is a binary operation that takes two equal-length sequences of numbers (usually coordinate vectors) and returns a single number.

![Alt text](<Screenshot from 2023-12-25 11-01-29.png>)
![Alt text](<Screenshot from 2023-12-25 11-01-42.png>)

`Graphically, it is the product of the length of one vector with the projection of the other vector on the first vector`. It can be used to evaluate how aligned two vectors are. It is also used to evaluate angle between vectors.


## FLOP/s
Vectors are stored as arrays of floating point numbers (or integers, when the entries are all integers). Storing an n-vector requires 8n bytes to store. Sparse vectors are stored in a more efficient way that keeps track of indices and values of the nonzero entries.

When computers carry out addition, subtraction,multiplication, division, or other arithmetic operations on numbers represented in floating point format, the result is rounded to the nearest floating point number.The very small error in the computed result is called (floating point) round-off error.These operations are called floating point operations.

A very rough estimate of the time required to carry out some computation, such as an inner product, can be found by counting the total number of floating point operations, or FLOPs. This is generally useful in evaluating complexity of algorithm and quality of hardware used.







