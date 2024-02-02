#  Splitwise Design

## **OVERVIEW**

> A expense sharing app where user can add an expense and distribute/divide it among a group of people.

## Requirements (As Suggested)

- User: Each user should have a userId, name, email, mobile number.

- Expense: Could either be EQUAL, EXACT or PERCENT

- Users can add any amount, select any type of expense and split with any of the
available users.

- The percent and amount provided could have decimals upto two decimal places.

- In case of percent, you need to verify if the total sum of percentage shares is 100 or not.

- In case of exact, you need to verify if the total sum of shares is equal to the total amount
or not.

- The application should have a capability to show expenses for a single user as well as
balances for everyone.

- When asked to show balances, the application should show balances of a user with all
the users where there is a non-zero balance.

- The amount should be rounded off to two decimal places. Say if User1 paid 100 and
amount is split equally among 3 people. Assign 33.34 to first person and 33.33 to
others.

- There should be an option to simplify expenses. When simplify expenses is turned on
(is true), the balances should get simplified. Ex: ‘User1 owes 250 to User2 and User2
owes 200 to User3’ should simplify to ‘User1 owes 50 to User2 and 200 to User3’.

- When a new expense is added, each participant in that expense should get an
email telling them that they have been added to an expense, the total amount they
owe for that expense. This email should be sent asynchronously (non-blocking)
so that the API call doesn't get blocked.

- A scheduled job that will send an email every week to users. This
email should contain the total amount of money they owe to each user.
Each expense can have up to 1000 participants and the maximum amount for an
expense can go up to INR 1,00,00,000/-

- All API responses should take less than 50 milliseconds.


## Optional Requirements (As Suggested)

- A way to add an expense name while adding the expense. Can also add notes,
images, etc.

- Option to split by share. Ex: ‘User4 pays and everyone splits equally. You pay for 2
people.’ could be added as: u4 1200 4 u1 u2 u3 u4 SHARE 2 1 1 1

- A way to show the passbook for a user. The entries should show all the transactions a
user was part of. You can print in any format you like.


### High Level Design for the given Requirements

![img.png](/home/milindsahu/Desktop/test/1/splitwise/Splitwise/splitwise/Templates/img.png)

### Database Schema for the given Requirements

![img_1.png](/home/milindsahu/Desktop/test/1/splitwise/Splitwise/splitwise/Templates/img_1.png)

- user 
