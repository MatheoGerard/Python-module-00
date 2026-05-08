# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgerard <mgerard@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/08 21:24:03 by mgerard           #+#    #+#              #
#    Updated: 2026/05/08 21:28:03 by mgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    last_water_day = input("Days since last watering: ")
    if int(last_water_day) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
