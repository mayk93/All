<%@ Page Language="C#" AutoEventWireup="true" CodeFile="edit.aspx.cs" Inherits="edit" %>

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
           <li><a href="#">About Us</a></li>
        </ul>
    </div>

    <form id="form1" runat="server">
        <div id="splitter" runat="server" style="width: 100%;">
            <div id="buttonDiv" runat="server" style="float:left; padding-right: 10%; width: 50%">
                <div id="textBoxDiv" runat="server" style="width: 70%; height: 70%; padding: 10%"><asp:TextBox ID="articleCodeBox" ValidateRequestMode="Disabled" TextMode="MultiLine" runat="server" Width ="100%" Height ="100%"></asp:TextBox></div>
                <asp:LinkButton ID="searchButton" runat="server" Text="" CssClass="btn btn-default" OnClick="Button1_Click">
                <i class='glyphicon glyphicon-cloud-upload'></i> Upload
                </asp:LinkButton>
            </div>

            <div id="codeAreaDiv" runat="server" style="float:right; padding-right: 10%; width: 50%"></div>
        </div>
    </form>

</body>
</html>
