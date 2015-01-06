<%@ Page Language="C#" AutoEventWireup="true" CodeFile="article.aspx.cs" Inherits="article" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
   <title></title>
   <link href="/Content/bootstrap.min.css" rel="stylesheet" />
   <script src="/Scripts/jquery.min.js"></script>
   <script src="/Scripts/bootstrap.min.js"></script>
</head>
<body>

    <div id="navigationDiv">
        <ul class="nav nav-tabs">
           <li><a href="main.aspx">Home</a></li>
           <li><a href="register.aspx">Register</a></li>
           <li><a href="login.aspx">Log In</a></li>
           <li class="active"><a href="search.aspx">Articles</a></li>
           <li><a href="edit.aspx">Edit</a></li>
           <li><a href="upload.aspx">Upload</a></li>
           <li><a href='search.aspx'>Search</a></li>
           <li><a href="#">About Us</a></li>
        </ul>
    </div>

    <form id="form1" runat="server">

    <div id="mainDiv" runat="server" align="center"></div>
    <br/>
    <div id="categoryDiv" runat="server" align="center"><p id ="categoryParagraph">Category: </p></div>

    </form>
</body>
</html>
