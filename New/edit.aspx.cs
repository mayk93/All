using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class edit : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<ArticleEdit> articleList;
    MongoCursor<ArticleEdit> articleCursor;

    ArticleEdit currentArticle;
    bool okToUpload = false;

    int currentArticleVersion;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.dataBaseInitialization();
        this.currentArticleVersion = Int32.Parse(Session["ArticleVersion"].ToString());
        this.loadArticleInformation();
    }

    public void loadArticleInformation()
    {
        int maxVersion = 0;
        foreach (ArticleEdit article in this.articleList)
        {
            if (article.articleName == Session["Article"].ToString())
            {
                if (article.version > maxVersion)
                {
                    maxVersion = article.version;
                }
            }
        }

        foreach (ArticleEdit article in this.articleList)
        {
            if (article.articleName == Session["Article"].ToString() && article.version == currentArticleVersion)
            {
                if (Session["UserRank"] != null)
                {
                    if (article.isProtected)
                    {
                        if (Int32.Parse(Session["UserRank"].ToString()) > 0)
                        {
                            codeAreaDiv.InnerText = article.articleContent;
                            this.currentArticle = article;
                            okToUpload = true;
                        }
                        else
                        {
                            codeAreaDiv.InnerText = "This article is protected.";
                        }
                    }
                    else
                    {
                        codeAreaDiv.InnerText = article.articleContent;
                        this.currentArticle = article;
                        okToUpload = true;
                    }
                }
                else
                {
                    if (article.isProtected)
                    {
                        codeAreaDiv.InnerText = "This article is protected.";
                    }
                    else
                    {
                        codeAreaDiv.InnerText = article.articleContent;
                        this.currentArticle = article;
                        okToUpload = true;
                    }
                }
            }
        }
    }

    public void dataBaseInitialization()
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("articleDataBase");
        this.collection = db.GetCollection<ArticleEdit>("Articles");

        this.articleCursor = this.collection.FindAllAs<ArticleEdit>();
        articleCursor.SetLimit(500);
        this.articleList = articleCursor.ToList();
    }

    protected void Button1_Click(object sender, EventArgs e)
    {
        String newContent = articleCodeBox.Text;
        if(okToUpload == true)
        {
            ArticleEdit newArticle = new ArticleEdit(this.currentArticle.version + 1, this.currentArticle.articleName, newContent , this.currentArticle.articleSubject, this.currentArticle.isProtected);
            this.collection.Save(newArticle);

            Session["Article"] = newArticle.articleName;
            Session["ArticleVersion"] = newArticle.version;

            Response.Redirect("main.aspx");
        }
    }
}

public class ArticleEdit
{
    public ObjectId Id { get; set; }
    public int version { get; set; }
    public String articleName { get; set; }
    public String articleContent { get; set; }
    public bool isProtected { get; set; }
    public String articleSubject { get; set; }
    public ArticleEdit(int version, String articleName, String articleContent, String articleSubject, bool isProtected)
    {
        this.version = version;
        this.articleName = articleName;
        this.articleContent = articleContent;
        this.articleSubject = articleSubject;
        this.isProtected = isProtected;
    }
}