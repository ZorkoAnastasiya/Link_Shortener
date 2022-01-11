# Задание
# 1. Необходимо написать запрос,
# который находит сколько ставок сыграло и не сыграло у каждого пользователя.


SELECT client_number, COUNT(win.outcome) AS Побед, COUNT(lose.outcome) AS Поражений
    FROM bid
    LEFT JOIN(
        SELECT * FROM event_value WHERE outcome = 'win'
    ) AS win
    ON win.play_id = bid.play_id AND win.value = coefficient
    LEFT JOIN(
        SELECT * FROM event_value WHERE outcome = 'lose'
    ) AS lose
    ON lose.play_id = bid.play_id AND lose.value = coefficient
    GROUP BY client_number
    ORDER BY client_number;


# 2. Необходимо написать запрос,
# который находит сколько раз между собой играли команды.
# Важно, если команда А играла против команды В,
# а затем команда В играла против команды А,
# то это считается как одно и тоже событие.
# То есть, результат должен быть следующим: А против В - 2 игры.


SELECT
    CASE
        WHEN home_team > away_team THEN home_team || '--' || away_team
        ELSE away_team || '--' || home_team
    END
    AS pairs_teams,
    COUNT(play_id) AS games_count
    FROM event_entity
    GROUP BY pairs_teams
    ORDER BY games_count;
