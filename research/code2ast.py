# coding: utf-8
import abc              # for definig abstract class
import sys
sys.path.append('..')
import os
import ast              # for creating ast of python code
import javalang         # for creating ast of java code
import networkx as nx   # for making graph
import matplotlib.pyplot as plt
import pygraphviz as pgv


class Code2AST(metaclass=abc.ABCMeta):

    # create abstract syntax tree from source code
    @abc.abstractmethod
    def code_to_ast(code):
        pass

    # convert created abstract syntxt tree to directed graph
    @abc.abstractmethod
    def ast_to_directed_graph(node, graph=None, parent=None):
        pass

    def draw_graph(graph, method='matplotlib'):
        print('='*50 + 'nodes of the graph' + '='*50)
        print(graph.nodes(data=True))
        if method == 'matplotlib':
            print(graph.nodes(data=True))
            pos = nx.spring_layout(graph, seed=42)
            node_labels = {node_id: data['type'] for node_id, data in graph.nodes(data=True)}
            nx.draw(graph, pos, with_labels=True, labels=node_labels)
            plt.show()
        elif method == 'graphviz':
            node_labels = {node_id: data['type'] for node_id, data in graph.nodes(data=True)}
            nx.set_node_attributes(graph, node_labels, 'label')
            graph = nx.nx_agraph.to_agraph(graph)
            graph.draw('ast.pdf', prog='dot', format='pdf')
            print('Drew and saved graph as ast.pdf.')
        else:
            print('\033[31m' + 'You must pick either matplotlib or graphviz in a method.' '\033[0m')


class PythonCode2AST(Code2AST):

    def code_to_ast(code):
        return ast.parse(code)

    def ast_to_directed_graph(node, parent=None, graph=None):
        if graph is None:
            graph = nx.DiGraph()

        node_type = type(node).__name__
        node_id = id(node)

        # set up node's attributes
        attributes = {
            'type': node_type
        }

        if isinstance(node, ast.Name):
            attributes['id'] = node.id # variable name, variable type
        if isinstance(node, ast.Constant):
            attributes['value'] = node.value
        if isinstance(node, ast.FunctionDef):
            attributes['name'] = node.name

        graph.add_node(node_id, **attributes)

        if parent is not None:
            graph.add_edge(id(parent), node_id)

        for child_node in ast.iter_child_nodes(node):
            PythonCode2AST.ast_to_directed_graph(child_node, node, graph)


        return graph


class JavaCode2AST(Code2AST):

    def code_to_ast(code):
        try:
            tree = javalang.parse.parse(code)
            return tree
        except javalang.parser.JavaSyntaxError:
            return None

    def ast_to_directed_graph(node, graph=None, parent=None):
        if graph is None:
            graph = nx.DiGraph()

        node_type = type(node).__name__
        node_id = id(node)

        # set up node's attributes
        attributes = {
            'type': node_type
        }

        if isinstance(node, javalang.tree.VariableDeclarator):
            attributes['name'] = node.name
        if isinstance(node, javalang.tree.Literal):
            attributes['value'] = node.value
        if isinstance(node, javalang.tree.PackageDeclaration):
            attributes['name'] = node.name
        if isinstance(node, javalang.tree.TypeDeclaration):
            attributes['name'] = node.name
        if isinstance(node, javalang.tree.MethodDeclaration):
            attributes['name'] = node.name
        if isinstance(node, javalang.tree.BinaryOperation):
            attributes['operator'] = node.operator

        graph.add_node(node_id, **attributes)

        if parent is not None:
            graph.add_edge(parent, node_id)

        # for child nodes of a node
        if isinstance(node, javalang.tree.Node):
            for field_name, field_value in node.__dict__.items():
                if isinstance(field_value, list):
                    for child_node in field_value:
                        if isinstance(child_node, javalang.tree.Node):
                            JavaCode2AST.ast_to_directed_graph(child_node, graph, node_id)
                        elif isinstance(field_value, javalang.tree.Node):
                            JavaCode2AST.ast_to_directed_graph(field_value, graph, node_id)

        return graph