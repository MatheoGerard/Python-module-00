# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgerard <mgerard@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/08 23:33:24 by mgerard           #+#    #+#              #
#    Updated: 2026/05/09 00:12:32 by mgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(current_days = 1, is_define = 0, days = 5):
    if not is_define:
        days = int(input("Days until harvest: "))
        is_define = 1
    if current_days <= days:
        print(f"Day {current_days}")
        ft_count_harvest_recursive(current_days + 1, is_define, days)
    else:
        print("Harvest time!")
