from aiogram.utils.callback_data import CallbackData

exhibitions_callback = CallbackData("exhibition", "exhibition_name", "exhibition_id", "db_exhibition_id")
exhibit_callback = CallbackData("exhibit", "exhibit_name", "exhibit_id", "exhibition_id", "db_exhibition_id")
exhibition_mode_callback = CallbackData("exhibition_choice", "choice_id", "choice_name")
excursion_mode_callback = CallbackData("exhibition_choice", "choice_id")
response_callback = CallbackData("response", "choice_id")  # 0 - dislike, 1 - like
navigation_callback = CallbackData("navigation", "direction")  #forward, backward, end
review_callback = CallbackData("review","user_id","excursion_id")
excursion_statistics_callback = CallbackData("statistics","user_id","excursion_id")
G_coins_callback = CallbackData("gcoins", "action", "amount") #get_current, #add_more


