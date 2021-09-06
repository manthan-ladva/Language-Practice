#------print & puts
# puts "Hii Manthan"
# print "Hello Manthan"
# print " How are you"

#------Drawing Shape
# puts "   /|"
# puts "  / |"
# puts " /  |"
# puts "/___|"

#------Variable
# character_name = "Manthan"
# character_age = "23"
# puts("Hii " + character_name)
# puts("His age is " + character_age)

#------Data Types
# name = "Manthan"
# age = 22
# ismale = true
# girlfriend = nil
# print(girlfriend)


#------Working with String
#name = "Manthan is Indian"
#puts name.upcase()
#puts name.downcase()
#puts name.length()
#puts name.include? "Indian"
#puts name.index('n')
#puts name[0,5]


#------Working with Numbers
#num = 22.45678575
#puts("Manthan's age is " + num.to_s)
#puts num.abs()
#puts num.round()
#puts Math.sqrt(36)
#puts Math.sin(90).ceil()


#------Input
# puts "Enter your Name: "
# name = gets.chomp()
# puts "Enter your age: "
# age = gets.chomp()
# puts("Hii " + name + ", Your age is " + age)


#--------Calculator
# puts "Give the value of Num1:"
# num1 = gets.chomp().to_f
# puts "Give the value of Num2:"
# num2 = gets.chomp().to_f
# puts(num1+num2)


#--------Array (List)
# friends = Array["Jatin", "Bharat", "Abhishek"]
# puts friends[0]
# puts friends.sort()
# puts friends
# puts friends.include? "Lucky"


#--------Hashes (Dictionary)
# states = {
#   :Gujarat => "GJ",
#   "Maharashtra" => "MH",
#   "Rajasthan" => "RJ"
# }
# puts states[:Gujarat]


#--------Methods (Function)
# def hey_there(name, age)
#   puts("Hey There " + name + ", You are " + age.to_s)
# end
#
# hey_there("Manthan", 22)


#--------Return in Function (Method)
# def cube(num)
#   return num*num*num
# end
#
# puts(cube(2.08).round())


#--------if else
# isMale = false
# isTall = false

# if isMale and isTall
#   puts "You are Male and Tall"
# elsif isMale and !isTall
#   puts "You are Male but not Tall"
# elsif !isMale and isTall
#   puts "You are Female and Tall"
# else
#   puts "You are Female and not Tall"
# end


#--------Case
# def abb(name)
#   day = ""
#   case name
#   when "mon"
#     day = "Monday"
#   when "tue"
#     day = "Tuesday"
#   else
#     day = "Invalid"
#   end
# end
#
# puts abb('fri')


#--------While Loop
# index = 1
# while index<=5
#   puts index
#   index+=1
# end


#--------For Loop
# friends = ["Abhishek", "Jatin", "Bharat", "Namrata"]
# for friend in friends
#   puts friends
# end

# friends.each do |friend|
#   puts friend
# end

# for index in 0..5
#   puts index
# end

#--------Exponent Methods
# def pow(base_num, power)
#   result = 1
#   # for i in 1..power
#   #   result*=base_num
#   # end
#   power.times do
#     result = result * base_num
#   end
#   return result
# end
#
# puts pow(5,5)


#--------Reading Files
# File.open("new.txt", 'r') do |file|
#   puts file.read()
# end

# file = File.open("new.txt", 'r')
# puts file.read()
# file.close()


#--------Exception Handling
# friends = [1,2,3,4,5,6,7,8,9]
# begin
#   num = 10/0
#   puts friends["Dog"]
# rescue ZeroDivisionError
#   puts "ZeroDivisionError"
# rescue TypeError
#   puts "Type Error"
# end


#--------Class Object

class Book
  attr_accessor :title, :author, :pages
  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end
end

book1 = Book.new("Harry Potter", "J K Rowling", 500)
puts book1.author
