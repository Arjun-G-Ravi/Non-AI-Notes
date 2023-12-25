# Linear System of Equation (S.O.L.E)
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

The matrix representation of a S.O.L.E can be changed to augmented matrix, and then represented in row echlon form. To do that, we can do three operations which will not change the solution set. They are called **elementary transformations**:
 - Multiply a row with a scalar
 - Add/sub a row with the multiple of another row
 - Interchange rows

If rank(A) == rank(augmented matrix) after converting both to row echlon form, then the system of linear eqns represented by the matrix is independent.
In row echlon form, the vectors are **generally** represented as rows in the coefficient matrix. Row operations are applied to the rows of the matrix to achieve the desired form, and the columns remain unchanged during this process.



# 6. Eigenvalues and Eigen vectors

Whenever we do a linear transformation, some vectors just remain in the line in which it spans out. Such vectors are called eigen vectors. The amount by which these eigenvectors are stretched are called eigen values.


Use: For a 3d rotation, the eigen vector will be the axis of rotation.

![Alt text](<Screenshot from 2023-12-24 11-45-21.png>)

We use this equation to compute the eigen value from eigen vectors.
![Alt text](<Screenshot from 2023-12-24 11-48-20.png>)

What this means is that transforming the vector v using A will yield the same result as multiplying the vector with a scalar value λ.
![Alt text](<Screenshot from 2023-12-24 11-55-37.png>)
And, only way two non zero matrices, becoming zero on matmul is if the det(A - λI) is zero. This would mean that the whole transformation squishes the space to a lower dimension.

Diagonal matrices have all basis as eigen vectors, with their eigen values being the diagonal values. This makes them super easy to work with.
![Alt text](<Screenshot from 2023-12-24 12-07-28.png>)