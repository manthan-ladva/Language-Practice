num.attacker.init <- 5
num.defender.init <- 2
num.attacker <- num.attacker.init
num.defender <- num.defender.init

battle.over <- FALSE
while(battle.over == FALSE){
  if(num.attacker <= 1){
    battle.over <- TRUE
    attacker.victory <- FALSE
  }
  else if(num.defender == 0){
    battle.over <- TRUE
    attacker.victory <- TRUE
  }
  else{
    num.attacker.dice <- getNumDice(num.attacker, 'attacker')
    num.defender.dice <- getNumDice(num.defender, 'defender')
    
    attacker.roll <- rollDice(num.attacker.dice)
    defender.roll <- rollDice(num.attacker.dice)
    
    battle.result <- getBattleResult(attacker.roll, defender.roll)
    
    num.attacker <- max(num.attacker - battle.result[1], 0)
    num.defender <- max(num.defender - battle.result[1], 0)
  }
}


getNumDice <- function(num.armies, players){
  if (players == 'attacker'){
    num.dice<- num.armies-1
    num.dice<- min(num.dice, 3)
  }
  else{
    num.dice<- min(num.armies, 2)
  }
  return(num.dice)
}


rollDice <- function(num.dice){
  possible.values <- 1:6
  rolls<- sample(x=possible.values, size = num.dice, replace = TRUE)
  return(rolls)
}


getBattleResult <- function(attacker.roll, defender.roll){
  attacker.roll <- sort(attacker.roll, decreasing = TRUE)
  defender.roll <- sort(defender.roll, decreasing = TRUE)
  num.dice.to.compare <- min(length(attacker.roll), length(defender.roll))
  attacker.roll <- attacker.roll[1:num.dice.to.compare]
  defender.roll <- defender.roll[1:num.dice.to.compare]
  dice.win <- attacker.roll > defender.roll
  defender.loose <- sum(dice.win)
  attacker.loose <- length(dice.win) - defender.loose
  result <- c(attacker.loose, defender.loose)
  return(result)
}
