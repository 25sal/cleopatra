#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import jsonpickle
import random
import datetime

from flask import Flask, jsonify, request, abort, make_response



class Singleton (type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class User:
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getIndex(self):
        return self.index


class UserManager(metaclass=Singleton):
    user_list = None
    user_index = 0

    def __init__(cls, *args):
        if len(args) == 1:
            user_list = args[0]
            if cls.user_list is None:
                cls.user_list = users_list
        elif len(args) ==0:
            cls.user_list = []


    def addNewUser(self, name):
        user = User(name, self.user_index)
        self.user_list.append(user)
        self.user_index += 1

    def getUserByName(self, name):
        for user in self.user_list:
            if user.getName() == name:
                return user
        return None

    def userPresence(self, name):
        for user in self.user_list:
            if user.getName() == name:
                return user.getName()
        return None

    def getUserIndex(self, name):
        for user in self.user_list:
            if user.getName() == name:
                return user.getIndex()
        return None

    def getUserList(self):
        name = []
        for u in self.user_list:
            name.append(u.getName())
        return name

    def getUserByIndex(self, index):
        for user in self.user_list:
            if user.getIndex() == index:
                return user
        return None


class TaskManager(metaclass=Singleton):
    # Vettore di N elementi contenente il testo dei task da completare
    Q = [
            "Cosa veneravano gli antichi egizi?",
            "Quante divintà erano presenti nel tempio funerario di Seti?",
            "La terza sala del museo è dedicata ad una divinità in particolare, chi è?",
            "Qual è il primo ruolo affibiato ad Anubi?",
            "Buona parte delle informazioni che abbiamo su questo popolo è dato dai loro manoscritti, su cosa erano riportati tali scritti?",
            "In quale regione è possibile trovare questa pianta in Italia?",
            "Un animale in particolare era ritenuto sacro, quale?"
        ]
    # Vettore di K elementi contenente l'indice dei task primari
    P = [0,2,4,6]
    # Vettore di N elementi contenente il task in cu si trova l'utente attualmente
    I = []
    # Vettore di N elementi dove ognuno rappresenta il task da portare a termine
    R = ["divinità","113","anubi","protettore delle tombe","papiro","sicilia","gatto"]
    # Vettore di N elementi rappresentanti le corrispettive tempistiche per terminare
    # un task
    T = [3,3,3,3]
    # Matrice di K*N elementi con K numero dei giocatori, N numero dei Task
    # Ogni riga sarà un vettore V, con parametri a 0 o 1 se l'utente ha comletato o meno quel task
    M = []
    # Vettore dei suggerimenti, contiene tutti i possibili suggerimenti che si possono fornire
    # durante l'esecuzione dell'i- esimo Task
    # A sua volta potremmo avere all'interno un vettore se è previsto più di un suggerimento
    S = [
            ["Ognuna rappresentava un aspetto della vita"],
            ["Troverai questa informazione in due liste esposte nella sala"],
            ["Ha assunto vari ruoli, prima imbalsamatore, poi protettore delle tombe","Ha la testa di sciacallo"],
            ["Poneva particolare attenzione sulle necropoli","Lo troverai nella prima parte della descrizione"],
            ["È ricavato da una pianta acquatica molto comune sul Nilo"],
            ["Ha bisogno di un clima caldo ed umido", "Regione del sud Italia"],
            ["È un felino"]
        ]
        # Matrice che riporta se l'utente ha già ricevuto suggerimenti e quanti per ogni task
    H = []
    # Numero di task
    N = 0
    # Vettore contenente curiosità sul museo
    curiosity = ['il museo è stato fondato nel 1800', 'il papa non è un re', 'pluto è  un cane']
    # Numero utenti
    users_number = 0
    # Variabile contenente il timestamp ad inizio gioco
    started = None
    MARGIN_TIME = 1

    def __init__(cls, users_number):
        cls.users_number = users_number
        cls.N = len(cls.R)
        # Inizializzo la matrice M a 0
        for i in range(0,users_number):
            row = []
            for j in range(0, cls.N):
                row.append(0)
            cls.M.append(row)
        # Inizializzo la matrice H a 0
        for i in range(0,users_number):
            row = []
            for j in range(0, cls.N):
                row.append(0)
            cls.H.append(row)
        for i in range(0,users_number):
            cls.I.append(0)
        cls.started = datetime.datetime.now()

    def getPrincipalTaskIndex(self, task_index):
        for i in range(0, len(self.P)-1):
            if task_index >= self.P[i] and task_index < self.P[(i+1)]:
                return [i,self.P[i]]
        return [i,self.P[len(self.P)-1]]

    def getNextPrincipalTask(self, value):
        for i in range(0, len(self.P)):
            if value == self.P[i]:
                return self.P[i+1]

    def checkQuestAnswer(self, task_index, answer):
        if task_index == len(self.R):
            return -1
        elif self.R[task_index] == answer:
            return True
        else:
            return False

    # Inserisco in quale task si trova ora l'utente
    def setUserTask(self, user_index, task_index):
        self.I[user_index] = task_index

    # Ritorna l'enigma
    def getTask(self, task_index):
        if task_index == len(self.Q):
            return -1
        return self.Q[task_index]

    # Ritorna l'indice del task in cui si trova l'utente
    def getUserQuestIndex(self, user_index):
        if self.I[user_index] == len(self.Q):
            return -1
        return self.I[user_index]

    def setCompletedQuest(self, user_index, task_index):
        if self.M[user_index][task_index] == 0:
            self.M[user_index][task_index] = 1
            return True
        return False

    def getTaskTip(self, task_index):
        if isinstance(self.S[task_index], list):
            tip_index = random.randint(0, len(self.S[task_index])-1)
            return self.S[task_index][tip_index]
        else:
            return self.S[task_index]
        return

    def getSingleUserTip(self, user_index, task_index):
        # Caso in cui abbiamo più di un suggerimento
        if  isinstance(self.S[task_index], list) and len(self.S[task_index]) > self.H[user_index][task_index]:
            help_index = self.H[user_index][task_index]
            self.H[user_index][task_index] += 1
            return self.S[task_index][help_index]
        elif not isinstance(self.S[task_index], list) and self.H[user_index][task_index] == 0:
            self.H[user_index][task_index] += 1
            return self.S[task_index]
        else:
            return -1

    def getUserIndexLessHelped(self):
        tmp = float('inf')
        user_index = -1
        for i in range(0, self.users_number):
            help = 0
            for j in range(0, self.N):
                help += self.H[i][j]
            if help < tmp:
                tmp = help
                user_index = i
        return user_index

    def getLateUser(self):
        task_index = float('inf')
        user_index = -1
        for i in range(0, self.users_number):
            last_task = -1
            for j in range(0, self.N):
                if self.M[i][j] == 1:
                    last_task = j
            if last_task < task_index:
                task_index = last_task
                user_index = i
        return [user_index, task_index+1]


    def checkIfIsLate(self, task_index):
        estimated_time = datetime.timedelta(minutes=0)
        print("Il ciclo for terminerà al giro {}".format(task_index))
        for i in range(0, task_index+1):
            print("Valore T[{}]={}".format(i, self.T[i]))
            estimated_time += datetime.timedelta(minutes = self.T[i])

        spent_time = datetime.datetime.now() - self.started

        # Ritorno 1 se è in ritardo
        if spent_time > estimated_time:
            return 1
        # Ritorno -1 se è in forte anticipo
        elif spent_time < (estimated_time-datetime.timedelta(minutes=self.MARGIN_TIME)):
            return -1
        # Ritorno 0 se è nei tempi previsti
        else:
            return 0

    def getPoints(self):
        P = []
        for i in range(0, self.users_number):
            tmp = 0
            for j in range(0, self.N):
                tmp += self.M[i][j]
            P.append([i,tmp])
        return P

    def getRandomCuriosity(self):
        rnd = random.randint(0, len(self.curiosity)-1)
        return self.curiosity[rnd]

class SharedStorage:
    app = Flask(__name__)

    def __init__(cls):
        cls.app.run()

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.route('/addNewUser/<user_name>', methods=['POST'])
    def addNewUserAPI(user_name):
        UserManager().addNewUser(user_name)
        return jsonpickle.encode({'success':True}), 200

    @app.route('/getPlayersNumber', methods=['GET'])
    def getPlayersNumber():
        return jsonpickle.encode(UserManager().getPlayersNumber())
    

    @app.route('/userPresence/<user_name>', methods=['GET'])
    def userPresence(user_name):
        return jsonpickle.encode(UserManager().userPresence(user_name))

    @app.route('/getNextQuest/<user_name>/<answer>', methods=['GET'])
    def getNextQuest(user_name, answer):
        user_index = UserManager().getUserIndex(user_name)
        task_index = TaskManager().getUserQuestIndex(user_index)
        if task_index == -1:
            return jsonpickle.encode(-1)
        if TaskManager().checkQuestAnswer(task_index, answer):
            TaskManager().setCompletedQuest(user_index, task_index)
            principal_index, principal_task_index = TaskManager().getPrincipalTaskIndex(task_index)
            if TaskManager().checkIfIsLate(principal_index) == -1:
                TaskManager().setUserTask(user_index, task_index+1)
                return jsonpickle.encode(TaskManager().getTask(task_index+1))
            else:
                next_task = TaskManager().getNextPrincipalTask(principal_task_index)
                TaskManager().setUserTask(user_index, next_task)
                return jsonpickle.encode(TaskManager().getTask(next_task))
        else:
            return jsonpickle.encode(False)

    @app.route('/getSingleUserTip/<user_name>', methods=['GET'])
    def getSingleUserTip(user_name):
        user_index = UserManager().getUserIndex(user_name)
        task_index = TaskManager().getUserQuestIndex(user_index)
        if task_index == -1:
            # Caso in cui l'utente ha terminato il gioco
            return jsonpickle.encode(-2)
        # Ritornerò -1 nel caso in cui sono finiti i tip
        return jsonpickle.encode(TaskManager().getSingleUserTip(user_index, task_index))

    @app.route('/getUserLessHelped', methods=['GET'])
    def getUserIndexLessHelped():
        user_index = TaskManager().getUserIndexLessHelped()
        user = UserManager().getUserByIndex(user_index)
        return jsonpickle.encode(user.getName())

    @app.route('/getRanking', methods=['GET'])
    def getRanking():
        P = TaskManager().getPoints()
        for i in range(0, len(P)):
            P[i][0] = UserManager().getUserByIndex(i).getName()
        # Ordinamento del vettore
        for i in range(0, len(P)):
            for j in range(i, len(P)):
                if P[j][1] > P[i][1]:
                    tmp = P[j]
                    P[j] = P[i]
                    P[i] = tmp
        return jsonpickle.encode(P)

    @app.route('/getHelpLateUser', methods=['GET'])
    def getHelpLateUser():
        [user_index, task_index] = TaskManager().getLateUser()
        user_name = UserManager().getUserByIndex(user_index).getName()
        if TaskManager().checkIfIsLate(task_index) == 1:
            tip = TaskManager().getTaskTip(task_index)
            return jsonpickle.encode([task_index, tip])
        return jsonpickle.encode(False)

    @app.route('/getRandomCuriosity', methods=['GET'])
    def getRandomCuriosity():
        return jsonpickle.encode(TaskManager().getRandomCuriosity())

def main():
    api = SharedStorage()


if __name__ == '__main__':
    main()
