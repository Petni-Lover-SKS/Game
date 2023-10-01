import random

def play_game():
    print("স্বাগতম! আমি Termux স্বচ্ছন্দের একটি ক্রিকেট গেম।")
    print("আমি দিঘার বোলা শুরু করছি, তুমি ব্যাট ধরো।")
    print("তুমি 1 থেকে 6 এর মধ্যে একটি সংখ্যা বেছে নিন এবং চালিয়ে দিন।")
    print("যদি তুমি ঠিক নাম্বারে ব্যাট দাও, তাহলে তুমি রান করবে।")
    print("আরও ভাল খেলতে চাও? চালছে? আগে যেখানে যেদিকে বলতে পেতে পারবেন সেখানে খেলা হয় এই গল্প এর মতো।")
    print("শুরু করার জন্য 'sks' লিখুন এবং Enter চাপুন।")
    
    user_input = input("")
    
    if user_input == "sks":
        total_score = 0
        while True:
            computer_number = random.randint(1, 6)
            user_number = int(input("দিন আপনার সংখ্যাটি (1-6): "))
        
            if user_number < 1 or user_number > 6:
                print("দুঃখিত, ভুল সংখ্যা! আবার চেষ্টা করুন।")
                continue
        
            print("আমার বলের সংখ্যা: ", computer_number)
            if user_number == computer_number:
                print("অভিনন্দন! তুমি রান করলে!")
                total_score += 1
            else:
                print("দুঃখিত! হিট হয়েছে। আপনার স্কোর: ", total_score)
                break
    else:
        print("খেলায় যোগদান করার জন্য শব্দটি সঠিকভাবে লিখুন।")

play_game()
