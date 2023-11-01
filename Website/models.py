from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Reservation(db.Model):  # Schema for Reservations
    id = db.Column(db.Integer, primary_key = True)
    TableNumber = db.Column(db.Integer(2),unique=True)
    PartySize = db.Column(db.Integer(2))
    TimeSlot = db.Column(db.Time())  #TimeSlot = db.Column(db.DateTime(timezone=True, default=func.now))
    Date = db.Column(db.DateTime())
    UserID = db.Column(db.Integer, db.ForeignKey('user.id'))


class Menu(db.Model): #Schema for menu
    id = db.Column(db.Integer,primary_key = True)
    Name = db.Column(db.String(100))
    Price = db.Column(db.Float(5))
    Description = db.Column(db.Text())
    ImagePath = db.Column(db.String(300))
    
    
class OrderItem(db.Model): #Schema for Item Ordered
    id = db.Column(db.Integer, primary_key = True)
    Quantity = db.Column(db.Integer(2))
    MenuID = db.Column(db.Integer(), db.ForeignKey('menu.id'))
    OrderID = db.Column(db.Integer(), db.ForeignKey('order.id'))
    
class Order(db.Model): #Schema for Order
    id = db.Column(db.Integer, primary_key = True)
    Status = db.Column(db.String(20))
    TotalPrice = db.Column(db.Float(8))
    CustomerName = db.Column(db.String(100))
    PhoneNumber = db.Column(db.String(20))
    EmailAddress = db.Column(db.String(100))
    Address = db.Column(db.String(400))
    Comments = db.Column(db.Text())
    PaymentMethod = db.Column(db.String(20))
    CreatedDate = db.Column(db.DateTime())
    ModifiedDate = db.Column(db.DateTime())
    Items = db.relationship("OrderItem", backref='orders')  # , lazy="dynamic"


class User(db.Model, UserMixin): #Schema for the User
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(256))
    FirstName = db.Column(db.String(30))
    LastName = db.Column(db.String(30))
    Reservation = db.relationship('Reservation')

