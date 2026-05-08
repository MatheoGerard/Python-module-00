# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgerard <mgerard@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/08 21:18:37 by mgerard           #+#    #+#              #
#    Updated: 2026/05/08 21:21:50 by mgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = input("Enter plant age in days: ")
    if int(age) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
