using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

using System.IO;

namespace BDAppTest
{
    public partial class Site1 : System.Web.UI.MasterPage
    {
        MongoClient client;
        MongoServer server;
        MongoDatabase db;
        MongoCollection collection;

        MongoClient clientArticle;
        MongoServer serverArticle;
        MongoDatabase dbArticle;
        MongoCollection collectionArticle;

        protected void Page_Load(object sender, EventArgs e)
        {
            this.client = new MongoClient();
            this.server = client.GetServer();
            this.db = server.GetDatabase("userDataBase");
            this.collection = db.GetCollection<User>("Users");

            this.clientArticle = new MongoClient();
            this.serverArticle = client.GetServer();
            this.dbArticle = server.GetDatabase("userDataBase");
            this.collectionArticle = db.GetCollection<User>("Users");

            this.loadArticles();
        }

        /* Register Button */
        protected void Button1_Click(object sender, EventArgs e)
        {
            if (Page.IsValid)
            {
                User newUser = new User(userField.Text, emailField.Text, passwordField.Text, 0);
                this.collection.Save(newUser);
            }
        }

        public void loadArticles()
        {
            string text = System.IO.File.ReadAllText(@"C:\Users\Mihai\Documents\DAW\Articles\0.txt");
            articleParagraph.InnerText = text;
            userListParagraph.InnerText = "";
        }

#region Useless
        protected void userField_TextChanged(object sender, EventArgs e)
        {

        }

        protected void emailField_TextChanged(object sender, EventArgs e)
        {

        }

        protected void passwordField_TextChanged(object sender, EventArgs e)
        {

        }

        protected void   passwordVerificationField_TextChanged(object sender, EventArgs e)
        {

        }
#endregion

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
}

/*
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using MongoDB.Bson;
using MongoDB.Driver;

namespace mongoTest
{
    class Program
    {
        static void Main(string[] args)
        {
            MongoClient client = new MongoClient();
            var server = client.GetServer();
            var db = server.GetDatabase("test");
            var collection = db.GetCollection<Book>("Book");

            Book book = new Book();
            book.Title = "Test Book";
            book.ISBN = 234245;
            book.Publisher = "Test Publisher";

            Book book0 = new Book();
            book0.Title = "Test Book 2";
            book0.ISBN = 4679;
            book0.Publisher = "Test PublisherXXX";

            Book book1 = new Book();
            book1.Title = "Test Book 3";
            book1.ISBN = 4679;
            book1.Publisher = "Test PublisherXXX";

            collection.Save(book);
            collection.Save(book0);

            Console.WriteLine("Col to Str: " + collection.ToString());
            Console.WriteLine("Col to JSon: " + collection.ToJson());
            Console.WriteLine("Here: " + collection.Count());
        }
    }
    public class Book
    {
        public ObjectId Id { get; set; }
        public int ISBN { get; set; }
        public string Title { get; set; }
        public string Publisher { get; set; }
    }
}

*/