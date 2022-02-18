# Portuguese Language Test
from seleniumbase.translate.portuguese import CasoDeTeste


class MinhaClasseDeTeste(CasoDeTeste):

    def test_exemplo_1(self):
        self.abrir("https://pt.wikipedia.org/wiki/")
        self.verificar_texto("Wikipédia")
        self.verificar_elemento('[title="Língua portuguesa"]')
        self.digitar("#searchInput", "João Pessoa")
        self.clique("#searchButton")
        self.verificar_texto("João Pessoa", "#firstHeading")
        self.verificar_elemento('img[alt*="João Pessoa"]')
        self.digitar("#searchInput", "Florianópolis")
        self.clique("#searchButton")
        self.verificar_texto("Florianópolis", "h1#firstHeading")
        self.verificar_elemento('img[alt*="Avenida Beira Mar"]')
        self.voltar()
        self.verificar_verdade("João" in self.obter_url_atual())
        self.digitar("#searchInput", "Teatro Amazonas")
        self.clique("#searchButton")
        self.verificar_texto("Teatro Amazonas", "#firstHeading")
        self.verificar_texto_do_link("Festival Amazonas de Ópera")
