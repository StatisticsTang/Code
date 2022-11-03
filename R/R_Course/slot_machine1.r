symbols <- c("C", "DD", "C")
#识别情形&计算中奖金额
if (symbols[1] == symbols[2] & symbols[1] == symbols[3]) {
  payouts <- c("DD" = 100, "7" = 80, "BBB" = 40, "BB" = 25, "B" = 10, "C" = 10, "0" = 0)
  prize <- unname(payouts[symbols[1]])
} else if (all(symbols %in% c("B", "BB", "BBB"))) {
  prize <- 5
} else {
  cherries <- sum(symbols == "C")
  prize <- c(0, 2, 5)[cherries + 1]
}

#根据钻石个数调整中奖金额
diamonds <- sum(symbols == "DD")
prize * 2 ^ diamonds