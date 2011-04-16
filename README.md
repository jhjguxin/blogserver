Blog based on Django
====

Screenshot
----
+ Blog
![Blog](./plandoc/blog.png)
+ About
![About](./plandoc/about.png)
+ Archive
![About](./plandoc/archive.png)

Function
----
+ About, show user resume by markdown.
+ Blog, user can view archive by Year/Month or by Tag.
+ Archives, show all archives by Category.
+ Category, user can view archive by Category. 
+ Tags, user can view archive by tag.
+ Feed, User can feed archive.
+ Backend admin
  + Archive admin
    + New, user can input the body by markdown.
    + Update, user can update the body by markdown and change Tag, Category
    + Delete, user can delete one 
  + Tag, CRUD
  + Category, CRUD

Layout
----

### Header
+ A logo | one words | Feed  
+ Blog | About | Archives

### Body
#### Left, Post 
+ Title  
+ Author | Publish Date | Category  
+ Tag  
+ Image  
+ Post Body

#### Right, Sidebar

+ Top, By Year/Month
+ Middle, By Category
+ Bottom, By Tag

### Footer
+ CopyRight 

Structure
----
+ app
    + blog
        + model
        + view
        + url
    + about
        + view
    
+ static
    + js
    + css
  
+ templates
    + blog
    + archive
    + about
  
+ locale
    + zh_CN
    
Url
----
+ index—An action that returns a listing of all resources; for example GET /urls will hit the index action on the URLs Controller, listing the known urls.
+ show—An action that performs a read operation for a single resource; for example GET /urls/1 will hit the show on the URLs Controller, showing the details of the URL with id 1.
+ new—The action to show a new object form, in our case, the new URL form; for example GET /urls/new will hit the new action on the URLs Controller and show the new URL form.
+ create—A post action to take the form data from the new action and to attempt to create a record; for example POST /urls will hit the create action on the URLs Controller, typically with some associated form data.
+ edit—Will show the form to edit a specific resource; for example GET /urls/1/edit will hit the edit action on the URLs Controller and show a form to edit the URL with id 1.
+ update—Will attempt to update the given resource; for example PUT /urls/1 will hit the update action on the URLs Controller and attempt to update the URL with id 1.
+ destroy—Will attempt to destroy a given resource; for example DELETE /urls/1 will hit the destroy action on the URLs Controller and attempt to destroy the URL with id 1.
