import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)

model=pickle.load(open("spam.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl", "rb"))

def main():
	st.title("Cassificador de E-mails Spam em inglês")
	st.subheader("Streamlit em Python")
	msg=st.text_input("Digite o Texto")
	if st.button("Verificar"):
		data=[msg]
		vect=cv.transform(data).toarray()
		prediction=model.predict(vect)
		result=prediction[0]
		if result==1:
			st.error("Esse é um E-mail Spam")
			speak("Esse é um E-mail Spam")
		else:
			st.success("Esse é um E-mail normal, não é um Spam")


main()