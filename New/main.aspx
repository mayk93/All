<%@ Page Language="C#" AutoEventWireup="true" CodeFile="main.aspx.cs" Inherits="main" %>

<!DOCTYPE html>
<html>

<head>
   <title>DAW Wiki</title>
   <link href="/Content/bootstrap.min.css" rel="stylesheet" />
   <script src="/Scripts/jquery.min.js"></script>
   <script src="/Scripts/bootstrap.min.js"></script>
</head>

<body>

    <div id="navigationDiv" runat="server"></div>

    <p>&nbsp;</p>

    <form id ="mainForm" runat="server">
        <div id="splitter" style="width: 100%;">

        <div id="dropDownMenuDiv" class="container" style="float:left; width: 50%">
          <h2>Welcome</h2>
          <p>This is an example wiki</p>                                          
          <div id="dropDownDiv" class="dropdown">
            <button class="btn btn-default dropdown-toggle" type="button" id="menu1" data-toggle="dropdown">Article Category
            <span class="caret"></span></button>
            <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">
              <li role="presentation"><a role="menuitem" tabindex="-1" href="art.aspx">Art</a></li>
              <li role="presentation"><a role="menuitem" tabindex="-1" href="history.aspx">History</a></li>
              <li role="presentation"><a role="menuitem" tabindex="-1" href="science.aspx">Science</a></li>
              <li role="presentation" class="divider"></li>
              <li role="presentation"><a role="menuitem" tabindex="-1" href="#">About Us</a></li>
            </ul>
          </div>
        </div>

        <div runat="server" id="articleDiv" style="float:right; padding-right: 10%; width: 50%"></div>

        </div>
    </form>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

    </body>
</html>

