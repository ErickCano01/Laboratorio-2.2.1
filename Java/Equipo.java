
package scrum;

import java.util.Vector;

public class Equipo {

    private String nombre;
    private int id;
    private ScrumMaster scrumMaster;
    public Vector<Integrante> integrantes = new Vector<Integrante>();

    public Equipo(String nombre, int id, ScrumMaster scrumMaster) {
        this.nombre = nombre;
        this.id = id;
        this.scrumMaster = scrumMaster;
    }

    
    
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String aNombre) {
        this.nombre = aNombre;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int aId) {
        this.id = aId;
    }

    public void addIntegrate(Integrante aIntegrante) {
        throw new UnsupportedOperationException();
    }


    public ScrumMaster getScrumMaster() {
        return this.scrumMaster;
    }

    public void setScrumMaster(ScrumMaster aScrumMaster) {
        this.scrumMaster = aScrumMaster;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Equipo{");
        sb.append("nombre=").append(nombre);
        sb.append(", id=").append(id);
        sb.append(", scrumMaster=").append(scrumMaster);
        sb.append(", integrantes=").append(integrantes);
        sb.append('}');
        return sb.toString();
    }

    
}
