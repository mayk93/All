using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class Register : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("userDataBase");
        this.collection = db.GetCollection<User>("Users");

        /*
        UserName.Text = "DefaultUser";
        UserMail.Text = "Default.Mail@Email.com";
        PassWord.Text = "defaultPassword";
        ConfirmPassWord.Text = "defaultPassword";
        */
    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        if (Page.IsValid)
        {
            User newUser = new User(UserName.Text, UserMail.Text, PassWord.Text, 1);
            this.collection.Save(newUser);

            Session["UserName"] = newUser.userName;
            Session["UserMail"] = newUser.userName;
            Session["UserRank"] = newUser.type;

            Response.Redirect("main.aspx");
        }
    }
}

public class User
{
    public ObjectId Id { get; set; }
    public String userName { get; set; }
    public String userMail { get; set; }
    public String userPassword { get; set; }
    public byte type { get; set; }
    public User(String userName, String userMail, String userPassword, byte type)
    {
        this.userName = userName;
        this.userMail = userMail;
        this.userPassword = userPassword;
        this.type = type;
    }
}