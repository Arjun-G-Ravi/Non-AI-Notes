# Linear Functions/ Linear Transformation/ Linear Mapping
It's a mathematical function between two vector spaces that preserves vector addition and scalar multiplication. Geometrically, a linear mapping takes vectors from one space to another in a way that maintains the structure of those vectors.
`Geometrically, it transforms the vector space such that the transformed grids are parallel and evenly spaced.The origin also retains its intitial position.`
Eg: Rotaion, Skew

![Alt text](<Screenshot from 2023-12-25 12-29-43.png>)

# Representation as Matrices

Transformation is generally represented as matrices where each column represent the new basis vector. Thus every vector in the initial space is matmuled with this transformation matrix to get the transformed vector.
![Alt text](<Screenshot from 2023-12-19 08-57-31.png>)

Multiplying two transformation matrix results in the combination of perfoming that both that linear transformation sequentially.

### Kernel/ Null space
The kernel of a linear transformation, also known as the null space, is the set of all vectors that map to the zero vector under that transformation. In other words, it consists of the inputs that get "flattened" to zero when the transformation is applied.

### Image
In the context of linear algebra and linear transformations, the term "image" refers to the set of all possible output values that a linear transformation can produce.  

### Rank
The number of linearly independent columns of a matrix equals the number of linearly independent rows and is called the rank of A and is denoted by rk(). When represented in the matrix form, it is the number of non-zero rows in echlon form.
`It represents the number of dimensions to which the vector space expands/compress after transformation.`

The rank of a matrix is a fundamental concept in linear algebra and is a measure of the "dimensionality" of the column space of the matrix. In simple terms, `the rank is the maximum number of linearly independent columns (or rows) in a matrix.` In other words, it quantifies how much "room" is occupied by the linearly independent vectors within the entire space.


