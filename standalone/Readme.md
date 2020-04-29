<p><span style="color: #000080;"><strong>Library Manager Flask REST API</strong></span></p>
<p><span style="color: #000080;"><strong>This is a standalone version of the library-manager</strong></span></p>
<p>With this API you can manage books with the following characteristic:</p>
<p><span style="text-decoration: underline;">Name</span>: The name of the book</p>
<p><span style="text-decoration: underline;">Price</span>: a value for the price</p>
<p><span style="text-decoration: underline;">ISBN</span>: the isbn unique code of the book</p>
<p>&nbsp;Supported request:</p>
<p>the following methods are supported for the interaction with the library-manager.</p>
<ul>
<li><strong>GET</strong>: To list all the available books make a call to the '/' route to get a list of all the stored books. You can also call the route '/books/isbn' to get the details of just one book</li>
</ul>
<p>&nbsp;</p>
<ul>
<li><strong>POST</strong>: To add a new book make a call to the '/books' route including a json body with the following structure:</li>
</ul>
<p>{'name': "a name", <br /> 'price': a price,<br /> 'isbn': a unique isbn<br /> }</p>
<ul>
<li><strong>PUT</strong>: To update all the values of a book, make a call to the '/books/isbn' route replacing 'isbn' with the isbn of the book that you want to update, including a body similar to:</li>
</ul>
<p>{'name': "a name", <br /> 'price': a price,<br /> 'isbn': a unique isbn<br /> }</p>
<ul>
<li><strong>PATCH: </strong>To update a single value of a book, make a call to the&nbsp;&nbsp;'/books/isbn' route replacing 'isbn' with the isbn of the book and include in the body a json file with the desired key and value to update</li>
</ul>
<p>&nbsp;</p>
<ul>
<li><strong>DELETE: </strong>To delete a book make a call to the '/books/&lt;int:isbn&gt;' route replacing the isbn with the one of the book that you want to delete.</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
