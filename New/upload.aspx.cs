using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class upload : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<ArticleUpload> articleList;
    MongoCursor<ArticleUpload> articleCursor;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.dataBaseInitialization();
    }

    public void dataBaseInitialization()
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("articleDataBase");
        this.collection = db.GetCollection<ArticleUpload>("Articles");

        this.articleCursor = this.collection.FindAllAs<ArticleUpload>();
        articleCursor.SetLimit(500);
        this.articleList = articleCursor.ToList();
    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        if (Page.IsValid)
        {
            ArticleUpload newArticle = new ArticleUpload(0, ArticleTitle.Text, ArticleContent.Text, ArticleCategory.Text, isProtectedBox.Checked);
            this.collection.Save(newArticle);

            Session["Article"] = newArticle.articleName;
            Session["ArticleVersion"] = newArticle.version;

            Response.Redirect("main.aspx");
        }
    }
    protected void CheckBox1_CheckedChanged(object sender, EventArgs e)
    {

    }
}

public class ArticleUpload
{
    public ObjectId Id { get; set; }
    public int version { get; set; }
    public String articleName { get; set; }
    public String articleContent { get; set; }
    public bool isProtected { get; set; }
    public String articleSubject { get; set; }
    public ArticleUpload(int version, String articleName, String articleContent, String articleSubject, bool isProtected)
    {
        this.version = version;
        this.articleName = articleName;
        this.articleContent = articleContent;
        this.articleSubject = articleSubject;
        this.isProtected = isProtected;
    }
}