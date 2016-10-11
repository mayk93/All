using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class login : System.Web.UI.Page
{

    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<UserLogIn> userList;
    MongoCursor<UserLogIn> userCursor;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("userDataBase");
        this.collection = db.GetCollection<UserLogIn>("Users");

        this.userCursor = this.collection.FindAllAs<UserLogIn>();
        userCursor.SetLimit(500);
        this.userList = userCursor.ToList();
    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        testDiv.InnerText = "Method Called";
        foreach(UserLogIn user in this.userList)
        {
            testDiv.InnerText = testDiv.InnerText + "\n" + user.userName + " : " + user.userPassword;
            if (user.userName == UserName.Text && user.userPassword == PassWord.Text)
            {
                testDiv.InnerText = "Found: " + user.userName + " : " + user.userPassword;

                Session["UserName"] = user.userName;
                Session["UserMail"] = user.userName;
                Session["UserRank"] = user.type;

                Response.Redirect("main.aspx");
            }
        }
    }
}

public class UserLogIn
{
    public ObjectId Id { get; set; }
    public String userName { get; set; }
    public String userMail { get; set; }
    public String userPassword { get; set; }
    public byte type { get; set; }
    public UserLogIn(String userName, String userMail, String userPassword, byte type)
    {
        this.userName = userName;
        this.userMail = userMail;
        this.userPassword = userPassword;
        this.type = type;
    }
}