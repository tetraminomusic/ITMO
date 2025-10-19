import mypokemons.*;
import ru.ifmo.se.pokemon.Battle;

public class Program {
    public static void main(String[] args) {
        Battle b = new Battle();


        Poliwag poliwag = new Poliwag("Solid Snake", 50);
        Virizion virizion = new Virizion("Maryl", 50);
        Cranidos cranidos = new Cranidos("Liquid Snake", 25);
        Politoed politoed = new Politoed("Revolver Ocelot", 30);
        Rampardos rampardos = new Rampardos("Otacon", 50);
        Poliwhirl poliwhirl = new Poliwhirl("Psycho Mantis", 40);


        b.addAlly(poliwag);
        b.addAlly(rampardos);
        b.addAlly(virizion);

        b.addFoe(politoed);
        b.addFoe(cranidos);
        b.addFoe(poliwhirl);

        b.go();
    }
}
