using System;

public class Tareas {
	private int id;
	private int prioridad;
	private String contexto;
    private Integrante encargado;

	public int GetId() {
		return this.id;
	}
	public void SetId(ref int id) {
		this.id = id;
	}
	public int GetPrioridad() {
		return this.prioridad;
	}
	public void SetPrioridad(ref int prioridad) {
		this.prioridad = prioridad;
	}
	public String GetContexto() {
		return this.contexto;
	}
	public void SetContexto(ref String contexto) {
		this.contexto = contexto;
	}
    public Integrante GetEncargado(){
        return this.encargado;
    }
    public void SetEncargado(Integrante encargado){
        this.encargado = encargado;
    }
    public Tareas(int id, int prioridad, String contexto, Integrante encargado){
        this.id = id;
        this.prioridad = prioridad;
        this.contexto = contexto;
        this.encargado = encargado;
    }
    public override String ToString() {
		return base.ToString() + "Id: "+ id.ToString() + "\n"+ "Prioridad: "+ prioridad.ToString() 
		+ "\n"+ "Contexto: "+ contexto.ToString() + "\n"
        + "\n"+ "Encargado: "+ encargado.ToString() + "\n";
	}


}