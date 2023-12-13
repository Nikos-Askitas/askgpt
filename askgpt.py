from openai import OpenAI
import os
import sys

class AUTH(object):

    def __init__(self, token):
        self.token = token
        
        
    def HeyChatGPT(self,myPrompt):
        client = OpenAI(api_key = self.token)
        myPrompt = myPrompt
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {
                  "role": "user",
                  "content": myPrompt
                    }
    
                    ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        return response.choices[0].message.content

    def ai(self,prompt):
        prompt = prompt
        answer = self.HeyChatGPT(prompt)
        import re
        from IPython.display import display, Javascript
        def add_cell(text,  type='code', direct='above'):
            text = text.replace('\n','\\n').replace("\"", "\\\"").replace("'", "\\'")

            display(Javascript('''
            var cell = IPython.notebook.insert_cell_{}("{}")
            cell.set_text("{}")
            '''.format(direct, type, text)));


        m=re.findall(r'```python(.+?)```',answer,re.DOTALL)
        if m:
            #print("ok")
            clean_answer = m[0].lstrip()
        else:
            clean_answer = answer.lstrip()
        
        def is_notebook():
            try:
                shell = get_ipython().__class__.__name__
                if shell == 'ZMQInteractiveShell':
                    return "jupyter"   # Jupyter notebook or qtconsole
                else:
                    return "lost"
            except:
                return os.path.realpath(__file__)

        if is_notebook() == "jupyter":
            add_cell(f'#chagpt says \n{clean_answer}')
        elif is_notebook() == "lost":
            print("bailing out")
        else:
            #print(is_notebook())
            #print(os.path.abspath(sys.argv[0]))
            file = open(os.path.abspath(sys.argv[0]),"a")
            file.write(f'\n##is this any good?##\n#chagpt says \n{clean_answer}#end chatgpt says')

