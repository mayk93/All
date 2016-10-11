<%@ Page Language="C#" AutoEventWireup="true" CodeFile="search.aspx.cs" Inherits="science" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Search</title>
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
           <li><a href='search.aspx' class="active">Search</a></li>
           <li><a href="#">About Us</a></li>
        </ul>
    </div>

    <div id="searchTitle" runat="server"><h2 style="text-align: center; padding-top: 5%">Search</h2></div>

    <form id="form1" runat="server" class="navbar-form navbar-left" role="search" style ="padding : 10%; padding-left : 40%;">

    <div class="form-group">
    <input id="searchInput" runat="server" type="text" class="form-control" placeholder="Search" style="width: 300px" />
    </div>
    <asp:LinkButton ID="searchButton" runat="server" Text="" CssClass="btn btn-default" OnClick="Button1_Click">
    <i class='glyphicon glyphicon-search'></i>
    </asp:LinkButton>

    </form>

</body>
</html>
