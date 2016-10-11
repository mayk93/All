<%@ Page Language="C#" AutoEventWireup="true" CodeFile="register.aspx.cs" Inherits="Register" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
   <title>Register</title>
   <link href="/Content/bootstrap.min.css" rel="stylesheet" />
   <script src="/Scripts/jquery.min.js"></script>
   <script src="/Scripts/bootstrap.min.js"></script>
    <style type="text/css">
        #registrationDiv {
            height: 455px;
        }
    </style>
</head>
<body>

    <div id="navigationDiv">
        <ul class="nav nav-tabs">
           <li><a href="main.aspx">Home</a></li>
           <li class="active"><a href="register.aspx">Register</a></li>
           <li><a href="login.aspx">Log In</a></li>
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
        <asp:TextBox ID="UserMail" runat="server" TextMode="Email"></asp:TextBox>
        <br/><br/>
        <asp:TextBox ID="PassWord" runat="server" TextMode="Password"></asp:TextBox>
        <br/><br/>
        <asp:TextBox ID="ConfirmPassWord" runat="server" TextMode="Password"></asp:TextBox>
        <asp:CompareValidator ID="PassWordValidator" ControlToValidate="PassWord" ControlToCompare="ConfirmPassWord" ErrorMessage="Please ensure the passwords match." runat="server"></asp:CompareValidator>
        <br/><br/>
        <asp:LinkButton ID="registrationButton" runat="server" Text="" CssClass="btn btn-default" OnClick="Button1_Click">
        <i class='glyphicon glyphicon-user'></i> Register
        </asp:LinkButton>

    </div>
    </form>

</body>
</html>
