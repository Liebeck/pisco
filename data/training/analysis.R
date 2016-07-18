trainingData = read.csv("training.txt", row.names = 1)

lapply(trainingData, mean)
# $neuroticism
# [1] 49.91837
# $extroversion
# [1] 45.22449
# $openness
# [1] 49.5102
# $agreeableness
# [1] 47.02041
# $conscientiousness
# [1] 46.36735

lapply(trainingData, sd)
# $neuroticism
# [1] 11.26913
# $extroversion
# [1] 8.274623
# $openness
# [1] 6.751921
# $agreeableness
# [1] 9.03809
# $conscientiousness
# [1] 6.527806