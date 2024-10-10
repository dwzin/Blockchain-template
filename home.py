import streamlit as st
from main import *

index_controller = 1

blockchain = Blockchain()

def HomePage():
    # page top
    st.header("Blockchain Example Project")

    st.markdown("---------------------------")
    st.write("Made by David Wendel , Github = https://github.com/dwzin")
    st.markdown("---------------------------")

    # page middle

    blocks_quantity = st.text_input("Qtd of Blocks")

    if st.button("Create Blocks"):
        try:
            qtd_blocks = int(blocks_quantity)
        except ValueError:
            st.error("Por favor, insira um número válido.")
            return

        execute_blocks(qtd_blocks)
    	
        st.subheader("Blocks")
        for block in blockchain.chain:
            st.write(f"Bloco {block.index} - Hash: {block.hash}, Dados: {block.data}, Nonce: {block.nonce}")



def execute_blocks(qtd):  
    global index_controller
    with st.expander("See Logs"):
        for i in range(qtd):
            new_block = Block(index=index_controller, previous_hash=blockchain.get_last_block().hash, data=f"Transaction {index_controller}")
            new_block.hash = blockchain.proof(new_block)
            blockchain.add_block(new_block)
            index_controller += 1
            st.success(f"Bloco {index_controller - 1} criado com sucesso.")

    if blockchain.check_chain():
        st.success("Blockchain válida")
    else:
        st.error("Blockchain inválida")


if __name__ == "__main__":
    HomePage()



