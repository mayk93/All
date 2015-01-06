<%@ Page Language="C#" AutoEventWireup="true" CodeFile="upload.aspx.cs" Inherits="upload" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
   <title>Upload</title>
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
           <li><a href="search.aspx">Articles</a></li>
           <li><a href="edit.aspx">Edit</a></li>
           <li class="active"><a href="upload.aspx">Upload</a></li>
           <li><a href='search.aspx'>Search</a></li>
           <li><a href="#">About Us</a></li>
        </ul>
    </div>

    <form id="form1" runat="server">
    <div id="uploadDiv" runat="server" style="padding: 5%">
    
        <asp:TextBox ID="ArticleTitle" runat="server"></asp:TextBox>
        <asp:RequiredFieldValidator ID="ArticleTitleValidator" ControlToValidate="ArticleTitle" ErrorMessage="Please insert a title." runat="server"></asp:RequiredFieldValidator>
        <br/><br/>
        <asp:TextBox ID="ArticleCategory" runat="server"></asp:TextBox>
        <asp:RequiredFieldValidator ID="ArticleCategoryValidator" ControlToValidate="ArticleCategory" ErrorMessage="Please insert a category." runat="server"></asp:RequiredFieldValidator>
        <br/><br/>
        <asp:TextBox ID="ArticleContent" runat="server" TextMode="MultiLine" ValidateRequestMode="Disabled"></asp:TextBox>
        <br/><br/>
        <asp:CheckBox ID="isProtectedBox" runat="server" OnCheckedChanged="CheckBox1_CheckedChanged" />
        <br/><br/>
        <asp:LinkButton ID="uploadButton" runat="server" Text="" CssClass="btn btn-default" OnClick="Button1_Click">
        <i class='glyphicon glyphicon-cloud-upload'></i> Upload
        </asp:LinkButton>

    </div>
    </form>

</body>
</html>
