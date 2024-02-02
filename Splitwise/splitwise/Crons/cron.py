
def email_user_weekly():
    # fetch users from the table daily and create ane event on message queue
    pass


if __name__ == "__main__":
    try:
        email_user_weekly()
    except Exception as e:
        raise e

