<%@ Page Language="C#" AutoEventWireup="true" CodeFile="login.aspx.cs" Inherits="login" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
   <title>Log In</title>
   <link href="/Content/bootstrap.min.css" rel="stylesheet" />
   <script src="/Scripts/jquery.min.js"></script>
   <script src="/Scripts/bootstrap.min.js"></script>
</head>
<body>

    <div id="navigationDiv">
        <ul class="nav nav-tabs">
           <li><a href="main.aspx">Home</a></li>
           <li><a href="register.aspx">Register</a></li>
           <li class="active"><a href="login.aspx">Log In</a></li>
           <li><a href="search.aspx">Articles</a></li>
           <li><a href="edit.aspx">Edit</a></li>
           <li><a href='search.aspx'>Search</a></li>
           <li><a href="#">About Us</a></li>
        </ul>
    </div>

    <form id="form1" runat="server">
    <div id="registrationDiv" runat="server" style="padding: 5%">
    
        <asp:TextBox ID="UserName" runat="server"></asp:TextBox>
        <asp:RequiredFieldValidator ID="UserNameValidator" ControlToValidate="UserName" ErrorMessage="Please insert an user name." runat="server"></asp:RequiredFieldValidator>
        <br/><br/>
        <asp:TextBox ID="PassWord" runat="server" TextMode="Password"></asp:TextBox>
        <br/><br/>
        <asp:LinkButton ID="logInButton" runat="server" Text="" CssClass="btn btn-default" OnClick="Button1_Click">
        <i class='glyphicon glyphicon-user'></i> Log In
        </asp:LinkButton>

    </div>

    <div id="testDiv" runat="server">Test</div>

    </form>

</body>
</html>
