<%@ Page Language="C#" AutoEventWireup="true" CodeFile="history.aspx.cs" Inherits="history" %>

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
           <li><a href="article.aspx">Articles</a></li>
           <li><a href="edit.aspx">Edit</a></li>
           <li><a href='search.aspx'>Search</a></li>
           <li><a href="#">About Us</a></li>
        </ul>
    </div>

    <form id="form1" runat="server">
    <div id="mainDiv" runat="server" align="center">
    </div>
    </form>
</body>
</html>
